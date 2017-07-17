pub mod monkey {
    pub mod lang {
        pub struct Parser {
        }

        impl Parser {
            pub fn println(&self) {
                println!("piyopiyo");
            }
        }
    }
}

use monkey::lang::Parser;

fn main() {
    let parser = Parser { };
    parser.println();
}