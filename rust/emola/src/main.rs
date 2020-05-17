mod emola {
    use std::fmt;
    pub enum Token {
        Plus,
        Minus,
        BracketStart,
        BracketEnd,
        Number(u32),
        Whitespace,
        Unknown,
    }

    impl fmt::Display for Token {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            match self {
                Token::Plus => write!(f, "{}", "+"),
                Token::Minus => write!(f, "{}", "-"),
                Token::BracketStart => write!(f, "{}", "("),
                Token::BracketEnd => write!(f, "{}", ")"),
                Token::Number(i) => write!(f, "{}", i),
                Token::Whitespace => write!(f, "{}", " "),
                Token::Unknown => write!(f, "{}", "Unknown"),
            }
        }
    }
}


fn main() {
    let inputs = "(+ 1 2)";
    {
        let tokens: Vec<emola::Token> = vec![];
        for c in inputs.chars() {
            let token: emola::Token = match c {
                '(' => emola::Token::BracketStart,
                ')' => emola::Token::BracketEnd,
                '+' => emola::Token::Plus,
                '-' => emola::Token::Minus,
                ' ' => emola::Token::Whitespace,
                mc => {
                    if mc.is_ascii_digit() {
                        emola::Token::Number(mc.to_digit(10).unwrap())
                    } else {
                        emola::Token::Unknown
                    }
                }
            };
            println!("{}", token);
        }
    }
}
