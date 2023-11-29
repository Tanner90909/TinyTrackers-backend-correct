FROM python:3.11
# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1
# Install any needed packages specified in requirements.txt
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
# Set up environment variables
ENV TRIGGER_REBUILD=3
ENV PGWORKSPACE="/workspace/.pgsql"
ENV PGDATA="$PGWORKSPACE/data"
# Install PostgreSQL
RUN echo "deb http://apt.postgresql.org/pub/repos/apt $(grep VERSION_CODENAME /etc/os-release | cut -d '=' -f 2)-pgdg main" > /etc/apt/sources.list.d/pgdg.list && \
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    apt-get update && apt-get install -y postgresql-12 postgresql-contrib-12
# Setup PostgreSQL server for user gitpod
ENV PATH="/usr/lib/postgresql/12/bin:$PATH"
SHELL ["/bin/bash", "-c"]
# Create a non-root user for PostgreSQL and switch to it
RUN useradd -m -d /var/lib/postgresql postgres_user && chown -R postgres_user:postgres_user /var/lib/postgresql
USER postgres_user
# Initialize the PostgreSQL database
RUN PGDATA="${PGDATA//\/workspace/$HOME}" \
 && mkdir -p ~/.pg_ctl/bin ~/.pg_ctl/sockets $PGDATA \
 && initdb -D $PGDATA \
 && printf '#!/bin/bash\npg_ctl -D $PGDATA -l ~/.pg_ctl/log -o "-k ~/.pg_ctl/sockets" start\n' > ~/.pg_ctl/bin/pg_start \
 && printf '#!/bin/bash\npg_ctl -D $PGDATA -l ~/.pg_ctl/log -o "-k ~/.pg_ctl/sockets" stop\n' > ~/.pg_ctl/bin/pg_stop \
 && chmod +x ~/.pg_ctl/bin/*
# Switch back to the root user
USER root
ENV PATH="$HOME/.pg_ctl/bin:$PATH"
ENV DATABASE_URL="postgresql://gitpod@localhost"
ENV PGHOSTADDR="127.0.0.1"
ENV PGDATABASE="postgres"
# Switch to the user gitpod and copy a script
# USER gitpod
# COPY --chown=gitpod:gitpod postgresql-hook.bash $HOME/.bashrc.d/200-postgresql-launch





