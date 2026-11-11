FROM python:3.10-slim

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64
ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-21-jdk-headless \
    openssh-server \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY hadoop-3.3.6.tar.gz /tmp/hadoop.tar.gz
RUN tar -xzf /tmp/hadoop.tar.gz -C /opt/ \
    && mv /opt/hadoop-${HADOOP_VERSION} ${HADOOP_HOME} \
    && rm /tmp/hadoop.tar.gz

# mkdir -p evita el error si el directorio /var/run/sshd ya existe
RUN mkdir -p /var/run/sshd \
    && ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa \
    && cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys \
    && chmod 600 /root/.ssh/authorized_keys

COPY start-hadoop.sh /usr/local/bin/start-hadoop.sh
RUN chmod +x /usr/local/bin/start-hadoop.sh

WORKDIR /app
EXPOSE 22

CMD ["/usr/local/bin/start-hadoop.sh"]
