# ------------------------------------------------------------------------------
# base with deps installed
# ------------------------------------------------------------------------------

FROM rust:latest as base

WORKDIR /usr/src/myapp

RUN apt-get update

RUN apt-get install musl-tools -y

RUN rustup target add x86_64-unknown-linux-musl

COPY Cargo* ./

RUN mkdir src/

RUN echo "fn main() {println!(\"if you see this, the build broke\")}" > src/main.rs

RUN RUSTFLAGS=-Clinker=musl-gcc cargo build --release --target=x86_64-unknown-linux-musl

RUN rm -f target/release/deps/dhtestingapp*

# ------------------------------------------------------------------------------
# prod build
# ------------------------------------------------------------------------------
FROM base as prod-build

RUN rm -rf target

COPY . .

RUN cargo install --target x86_64-unknown-linux-musl --path .

# RUN RUSTFLAGS=-Clinker=musl-gcc cargo build --release --target=x86_64-unknown-linux-musl

# ------------------------------------------------------------------------------
# prod stage
# ------------------------------------------------------------------------------

FROM scratch as prod

COPY --from=prod-build /usr/local/cargo/bin/dhtestingapp .

ENTRYPOINT [ "./dhtestingapp" ]