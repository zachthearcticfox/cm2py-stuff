use image;
use image::GenericImageView;

fn main() {
    let img = image::open("../me.png").expect("OS Error")
    println!(img.pixels())
}