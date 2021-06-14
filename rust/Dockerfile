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

RUN cargo build --release --target=x86_64-unknown-linux-musl

RUN rm -f target/release/deps/dhtestingapp*

# ------------------------------------------------------------------------------
# dev build
# ------------------------------------------------------------------------------
FROM base as dev
RUN rustup component add rust-src --toolchain 1.52.1-x86_64-unknown-linux-gnu
RUN rustup component add rls --toolchain 1.52.1-x86_64-unknown-linux-gnu
RUN rustup component add rust-analysis --toolchain 1.52.1-x86_64-unknown-linux-gnu

# ------------------------------------------------------------------------------
# prod build
# ------------------------------------------------------------------------------

FROM base as prod-build

COPY . .

RUN cargo build --release --target=x86_64-unknown-linux-musl

# ------------------------------------------------------------------------------
# prod stage
# ------------------------------------------------------------------------------

FROM scratch as prod

EXPOSE 8080

COPY --from=prod-build /usr/src/myapp/target/x86_64-unknown-linux-musl/release/dhtestingapp .

ENTRYPOINT [ "./dhtestingapp" ]
