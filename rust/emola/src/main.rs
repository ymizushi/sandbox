mod emola {
    use std::fmt;
    pub enum Token {
        Plus,
        Minus,
        BracketStart,
        BracketEnd,
        Number(u32),
        Unknown,
    }

    pub enum AST {
        Tree(Vec<AST>),
        Leaf(Token),
    }

    impl fmt::Display for Token {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            match self {
                Token::Plus => write!(f, "{}", "+"),
                Token::Minus => write!(f, "{}", "-"),
                Token::BracketStart => write!(f, "{}", "("),
                Token::BracketEnd => write!(f, "{}", ")"),
                Token::Number(i) => write!(f, "{}", i),
                Token::Unknown => write!(f, "{}", "Unknown"),
            }
        }
    }

    pub fn parse(tokens: Vec<Token>) -> Vec<AST> {
        tokens.into_iter().map(|t| {
            let token: AST = match t {
                Token::Plus => AST::Leaf(Token::Plus),
                Token::Minus => AST::Leaf(Token::Minus),
                Token::BracketStart => AST::Tree(vec![]),
                Token::BracketEnd => AST::Leaf(Token::Plus),
                Token::Number(i) => AST::Leaf(Token::Number(i)),
                Token::Unknown => AST::Leaf(Token::Plus),
            };
            token
        }).collect()
    }
}


fn main() {
    let inputs = "(+ 10 20 30)";
    let mut tokens: Vec<emola::Token> = vec![];
    let mut current_string: String = "".to_string();
    let replaced_inputs = inputs.replace("(", " ( ").replace(")", " ) ");
    let chars = replaced_inputs.chars();
    for c in chars {
        let token: emola::Token = match c {
            '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' => {
                current_string.push(c);
                continue;
            },
            '(' => emola::Token::BracketStart,
            ')' => emola::Token::BracketEnd,
            '+' => emola::Token::Plus,
            '-' => emola::Token::Minus,
            ' ' => {
                if current_string.len() != 0 {
                    let num = current_string.parse().unwrap();
                    current_string.truncate(0);
                    emola::Token::Number(num)
                } else {
                    continue;
                }
            },
            _ => emola::Token::Unknown
        };
        println!("{}", token);
        tokens.push(token);
    }
}
