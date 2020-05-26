use std::collections::HashMap;
use std::option::Option::*;

#[derive(Debug, PartialEq)]
pub struct Env<'a> {
    env: HashMap<&'a String, &'a String>,
    outer: Option<Box<Env<'a>>>
}

impl<'a> Env<'a> {
    pub fn new() -> Env<'a> {
        Env {
            env: HashMap::new(),
            outer: None
        }
    }

    pub fn find(&self, key: String) -> Option<&Env<'a>> {
        match self.env.get(&key) {
            Some(_) => Some(&self),
            None => {
                match &self.outer {
                    Some(env) => env.find(key),
                    None => None
                }
            }
        }
    }
}


#[derive(Debug)]
pub enum Token {
    Plus,
    Minus,
    BracketStart,
    BracketEnd,
    Number(u32),
    Unknown,
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn env_find() {
        let env = Env::new();
        let result = env.find(String::from("unknown"));
        assert_eq!(result, None);

    }
}
