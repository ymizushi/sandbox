pub enum TokenType {
    LET,
    UNKNOWN
}

impl TokenType {
    pub fn to_string(&self) -> String {
        return String::from("hoge");
    }
    pub fn from_string(s: String) -> TokenType {
        match s.as_ref() {
            "LET" => TokenType::LET,
            _ => TokenType::UNKNOWN,
        }
    }
}


pub struct Token {
    pub token_type: TokenType
}

impl Token {
    pub fn to_string(&self) {
        println!("token_type: {}", self.token_type.to_string());
    }
}


pub struct Parser {}

impl Parser {
    pub fn println(&self) {
        println!("piyopiyo");
    }
}
