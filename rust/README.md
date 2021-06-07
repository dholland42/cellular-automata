# 1D Cellular Automata in Rust

This code implements simple 1-dimensional elementary cellular automata
in Rust and wraps the logic in a simple web server. The main logic for
evolving cell states lives in `src/ca.rs`, while the web server logic
lives in the main file - `main.rs`. The `models.rs` file simply implements
the `State` struct which we expect to receive from POST requests.

## VSCode Stuff
This code is set up for ease of use with VSCode using development containers.
To get up an running quickly, get VSCode and install the remote-containers
extension. Then, simply open this location with VSCode and you should be prompted
to reopen inside a container. The first time you do this, the container will
need to be built, so it may take a minute. However, once you do you should be
all set up in an environment that contains Rust, cargo, etc.

## Docker Stuff
This is a neat experiment for myself in creating standalone binaries. Through
multistage docker builds, we can use a single `Dockerfile` to define both our
development environment and our production environment. More than that, we can
link the two together. Our developoment environment will come with everything
we could need - an ubuntu-based OS, Rust, cargo, and all that jazz. However,
with Rust we are able to compile to a static binary using `musl`. This will
allow our binary to run in the extremely minimal `scratch` docker image, which
we will use as a production base. This means that our final production docker
image size is aroung 10MB.