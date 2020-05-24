use wasm_bindgen::prelude::*;
use yew::prelude::*;

use svg::Document;
use svg::node::element::Path;
use svg::node::element::path::Data;

fn svg() -> Document {
    let data = Data::new()
        .move_to((10, 10))
        .line_by((0, 50))
        .line_by((50, 0))
        .line_by((0, -50))
        .close();
    
    let path = Path::new()
        .set("fill", "none")
        .set("stroke", "black")
        .set("stroke-width", 3)
        .set("d", data);
    
    Document::new()
        .set("viewBox", (0, 0, 70, 70))
        .add(path)

}

struct Model {
    link: ComponentLink<Self>,
    value: i64,
}

enum Msg {
    AddOne,
}

impl Component for Model {
    type Message = Msg;
    type Properties = ();
    fn create(_: Self::Properties, link: ComponentLink<Self>) -> Self {
        Self {
            link,
            value: 0,
        }
    }

    fn update(&mut self, msg: Self::Message) -> ShouldRender {
        match msg {
            Msg::AddOne => self.value += 1
        }
        true
    }

    fn change(&mut self, _props: Self::Properties) -> ShouldRender {
        // Should only return "true" if new properties are different to
        // previously received properties.
        // This component has no properties so we will always return "false".
        false
    }

    fn view(&self) -> Html {
        html! {
            <div>
                <button onclick=self.link.callback(|_| Msg::AddOne)>{ "+1" }</button>
                <p>{ self.value }</p>
                <p>{ svg().to_string() }</p>
                <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
                <path d="M10,10 l0,50 l50,0 l0,-50 z" fill="none" stroke="black" stroke-width="3"/>
                </svg>
            </div>

        }
    }
}

#[wasm_bindgen(start)]
pub fn run_app() {
    App::<Model>::new().mount_to_body();
}
