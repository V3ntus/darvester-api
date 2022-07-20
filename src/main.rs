use rocket::{Build, Rocket, Request};
#[macro_use] extern crate rocket;

#[catch(404)]

#[get("/")]
fn index() -> &'static str {
    "Hello, world!"
}

#[launch]
fn rocket() -> Rocket<Build> {
    rocket::build()
        .mount("/", routes![index])
}
