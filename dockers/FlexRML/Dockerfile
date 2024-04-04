################################################################################
# FlexRML
# https://github.com/wintechis/flex-rml
################################################################################
FROM ubuntu:22.04

# Install latest updates and dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget

# Download FlexRML release
RUN mkdir flexrml && wget -O flexrml/FlexRML https://github.com/wintechis/flex-rml/releases/download/1.0.0/FlexRML_Ubuntu_x64

# Make it executable
RUN chmod 755 /flexrml/FlexRML

# Expose data folder
RUN mkdir /data

# Silent
CMD ["tail", "-f", "/dev/null"]