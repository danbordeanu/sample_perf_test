# Pull base image.
FROM /ubuntu/18.04/

#tzda
ENV TZ=Europe/Prague
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


#let's update
RUN apt-get update

#let's install the internet
RUN apt-get install -y --force-yes \
		apt-utils \ 
		wget \
		telnet \
		curl \
		python \
		python-pip \
		curl \
		apache2-utils \
	&& rm -rf /var/lib/apt/lists/*


# let's add multimech tests
COPY . /home/

# let's install python dependencies list
RUN pip install -r /home/requirements.txt

WORKDIR /home/

# Define default command.
CMD ["/bin/bash"]
