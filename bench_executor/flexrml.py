#!/usr/bin/env python3

"""
FlexRML a flexible and memory-efficient knowledge graph materializer. 

**Repository**: https://github.com/wintechis/flex-rml/
"""

import os
import psutil
from typing import Optional
from timeout_decorator import timeout, TimeoutError  # type: ignore
from bench_executor.logger import Logger
from bench_executor.container import Container

TIMEOUT = 6 * 3600  # 6 hours

class FlexRML(Container):
    """FlexRML container for executing mappings."""

    def __init__(
        self,
        data_path: str,
        config_path: str,
        directory: str,
        verbose: bool,
        expect_failure: bool = False,
    ):
        """Creates an instance of the flexrml class.

        Parameters
        ----------
        data_path : str
            Path to the data directory of the case.
        config_path : str
            Path to the config directory of the case.
        directory : str
            Path to the directory to store logs.
        verbose : bool
            Enable verbose logs.
        expect_failure : bool
            If a failure is expected, default False.
        """
        self._data_path = os.path.abspath(data_path)
        self._config_path = os.path.abspath(config_path)
        self._logger = Logger(__name__, directory, verbose)
        self._verbose = verbose

        os.makedirs(os.path.join(self._data_path, "flexrml"), exist_ok=True)
        super().__init__(
            f"freumi/flexrml",
            "flexrml",
            self._logger,
            expect_failure=expect_failure,
            volumes=[
                f"{self._data_path}/flexrml:/data",
                f"{self._data_path}/shared:/data/shared",
            ],
        )

    @property
    def root_mount_directory(self) -> str:
        """Subdirectory in the root directory of the case for RMLMapper.

        Returns
        -------
        subdirectory : str
            Subdirectory of the root directory for RMLMapper.

        """
        return __name__.lower()

    @timeout(TIMEOUT)
    def _execute_with_timeout(self, arguments: list) -> bool:
        """Execute a mapping with a provided timeout.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        # Execute command
        cmd = f"/flexrml/FlexRML"
        cmd += f' {" ".join(arguments)}'

        self._logger.debug(
            f"Executing FlexRML with arguments " f'{" ".join(arguments)}'
        )
        return self.run_and_wait_for_exit(cmd)

    def execute(self, arguments: list) -> bool:
        """Execute FlexRML with given arguments.

        Parameters
        ----------
        arguments : list
            Arguments to supply to FlexRML.

        Returns
        -------
        success : bool
            Whether the execution succeeded or not.
        """
        try:
            return self._execute_with_timeout(arguments)
        except TimeoutError:
            msg = f"Timeout ({TIMEOUT}s) reached for FlexRML"
            self._logger.warning(msg)

        return False

    def execute_mapping(
        self,
        mapping_file: str,
        output_file: str,
    ) -> bool:
        """Execute a mapping file with FlexRML.

        N-Quads and N-Triples are currently supported as serialization
        format for RMLMapper.

        Parameters
        ----------
        mapping_file : str
            Path to the mapping file to execute.
        output_file : str
            Name of the output file to store the triples in.

        Returns
        -------
        success : bool
            Whether the execution was successfull or not.
        """
        arguments = [
            "-m",
            os.path.join("/data/shared/", mapping_file),  # Set mapping file
            "-o",
            os.path.join("/data/shared/", output_file),  # Set output file
            "-d",  # Enable duplicate removal
            "-t",  # Enable threading
            "-a",  # Enable adaptive hash selection
            "-p",  # Set sampling probability to 0.02
            "0.02",
            "-r",  # Remove NULL values
            "NULL",
        ]

        return self.execute(arguments)
