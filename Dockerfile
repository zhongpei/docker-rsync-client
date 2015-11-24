FROM debian:jessie
#
# Set correct environment variables.
ENV HOME /data

RUN apt-get update && apt-get install -y software-properties-common python-software-properties && apt-get update\
	&& apt-get install -yq --no-install-recommends rsync\
	&& apt-get install -y python cron\
	&& apt-get purge -y python-software-properties software-properties-common && apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD cron-python /etc/cron.d/
# Set the time zone to the local time zone
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

WORKDIR /data
CMD ["cron","-f","-L 15"]
