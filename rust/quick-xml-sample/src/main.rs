use quick_xml::Writer;
use quick_xml::events::{Event, BytesEnd, BytesStart};
use quick_xml::Reader;
use std::io::Cursor;

fn main() {
	let xml = r#"<this_tag k1="v1" k2="v2"><child>text</child></this_tag>"#;
	let mut reader = Reader::from_str(xml);
	reader.trim_text(true);
	let mut writer = Writer::new(Cursor::new(Vec::new()));
	let mut buf = Vec::new();
	loop {
	    match reader.read_event(&mut buf) {
	        Ok(Event::Start(ref e)) if e.name() == b"this_tag" => {
	
	            // crates a new element ... alternatively we could reuse `e` by calling
	            // `e.into_owned()`
	            let mut elem = BytesStart::owned(b"my_elem".to_vec(), "my_elem".len());
	
	            // collect existing attributes
	            elem.extend_attributes(e.attributes().map(|attr| attr.unwrap()));
	
	            // copy existing attributes, adds a new my-key="some value" attribute
	            elem.push_attribute(("my-key", "some value"));
	
	            // writes the event to the writer
	            assert!(writer.write_event(Event::Start(elem)).is_ok());
	        },
	        Ok(Event::End(ref e)) if e.name() == b"this_tag" => {
	            assert!(writer.write_event(Event::End(BytesEnd::borrowed(b"my_elem"))).is_ok());
	        },
	        Ok(Event::Eof) => break,
	        Ok(e) => assert!(writer.write_event(e).is_ok()),
	        // or using the buffer
	        // Ok(e) => assert!(writer.write(&buf).is_ok()),
	        Err(e) => panic!("Error at position {}: {:?}", reader.buffer_position(), e),
	    }
	    buf.clear();
	}
	
	let result = writer.into_inner().into_inner();
	let expected = r#"<my_elem k1="v1" k2="v2" my-key="some value"><child>text</child></my_elem>"#;
	assert_eq!(result, expected.as_bytes());
}
