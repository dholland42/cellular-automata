// Just a simple web server that evolves a state

mod ca;
mod models;

use crate::ca::{get_all_mappings};
use crate::models::{State};

use actix_web::{post, web, middleware, App, HttpResponse, HttpServer, Responder};
use env_logger;


#[post("/")]
async fn index(data: web::Data<ca::Rules>, info: web::Json<State>) -> impl Responder {
    HttpResponse::Ok()
    .json(State {
        state: data.evolve(&info.state, &info.rule),
        rule: info.rule,
    })
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=debug");
    env_logger::init();
    HttpServer::new(|| {
        App::new()
            .data(ca::Rules{rules: get_all_mappings()})
            .wrap(middleware::Logger::default())
            .service(index)
    })
    .bind("0.0.0.0:8080")?
    .run()
    .await
}