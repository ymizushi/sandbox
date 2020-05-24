use quick_xml::Writer;
use quick_xml::events::{Event, BytesEnd, BytesStart};
use std::io::Cursor;
use std::result::Result;

fn main() {
	let mut writer = Writer::new(Cursor::new(Vec::new()));
    let mut elem = BytesStart::owned(b"my_elem".to_vec(), "my_elem".len());
    elem.push_attribute(("my-key", "some value"));
    if let Result::Err(e) =  writer.write_event(Event::Start(elem)) {
        panic!("{}", e)
    }
    if let Result::Err(e) =  writer.write_event(Event::End(BytesEnd::borrowed(b"my_elem"))) {
        panic!("{}", e)
    }
	let result = writer.into_inner().into_inner();
    let s: String = result.into_iter().map(|u| { char::from(u) }).collect();
    println!("{}", s);
}
