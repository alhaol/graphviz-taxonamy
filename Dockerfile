FROM python:3.9


USER root
# Create the user 'ibrahim' and set password to 'dellwin'
RUN useradd -m ibrahim && echo "ibrahim:dellwin" | chpasswd

# Give ibrahim sudo power
RUN usermod -aG sudo ibrahim

USER ibrahim 
# Set the working directory
WORKDIR /home/ibrahim/app

RUN mkdir -p /home/ibrahim/app/.local

# Set the ownership of the '/home/ibrahim/app' directory to 'ibrahim'
RUN sudo chown -R ibrahim:ibrahim /home/ibrahim/app /home/ibrahim/app/.local

# Install necessary packages and dependencies
RUN sudo apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Jupyter Lab using pip
RUN pip install jupyterlab

# Set the environment variable for graphviz
ENV PATH=$PATH:/usr/bin/graphviz
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/graphviz

# Switch to the non-root user 'ibrahim'
#USER ibrahim

# Mount a host directory as a volume
VOLUME /home/ibrahim/app

# Start the Jupyter Lab server
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser","--allow-root"]
