fn main() {
    println!("hoge {}", 5);
    foo();
}

struct BigInt {
    i: i32
}

impl Clone for BigInt {
    fn clone(&self) -> Self {
        return BigInt {
            i: self.i
        }
    }
}

fn foo() {
    let v = vec![1, 2, 3];
    println!("{}", v[0]);
    let bi = BigInt {i: 10};
    let hoge = bi.copy();
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
    }
}
