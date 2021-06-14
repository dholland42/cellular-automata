// Just a simple web server that evolves a state

mod ca;
mod models;

use crate::ca::{evolve};
use crate::models::{State};

use actix_web::{post, web, middleware, App, HttpResponse, HttpServer, Responder};
use env_logger;


#[post("/")]
async fn index(info: web::Json<State>) -> impl Responder {
    HttpResponse::Ok()
    .json(State {
        state: evolve(&info.state, &info.rule),
        rule: info.rule,
    })
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    std::env::set_var("RUST_LOG", "actix_web=debug");
    env_logger::init();
    HttpServer::new(|| {
        App::new()
            .wrap(middleware::Logger::default())
            .service(index)
    })
    .bind("0.0.0.0:8080")?
    .run()
    .await
}

// fn dothing(&x: &u32) -> u32  {
//     println!("{}", x);
//     x
// }

// fn main() {
//     let x = 10;
//     dothing(&x);
// }