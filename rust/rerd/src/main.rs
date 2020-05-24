use quick_xml::Writer;
use quick_xml::events::{Event, BytesEnd, BytesStart};
use std::io::Cursor;
use std::result::Result;

fn main() {
	let mut writer = Writer::new(Cursor::new(Vec::new()));
    let mut elem = BytesStart::owned(b"svg".to_vec(), "svg".len());
    elem.push_attribute(("width", "100"));
    elem.push_attribute(("height", "100"));
    if let Result::Err(e) =  writer.write_event(Event::Start(elem)) {
        panic!("{}", e)
    }
    if let Result::Err(e) =  writer.write_event(Event::End(BytesEnd::borrowed(b"svg"))) {
        panic!("{}", e)
    }
	let result: Vec<u8> = writer.into_inner().into_inner();
    let s = result.clone().into_iter().map(|u| { char::from(u) }).collect::<String>();
    println!("{}", s);
}
