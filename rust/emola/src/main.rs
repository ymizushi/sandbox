
fn main() {
  println!("{}", sum(5));
  println!("{}", join("hoge", "piyo"));
}

fn join(left: &str, right: &str) -> String {
  let mut s = String::new();
  s.push_str(left);
  s.push_str(right);
  s
}

fn sum(n: i64) -> i64 {
  match n {
    1 => 1,
    _ => n + sum(n-1)
  }
}
