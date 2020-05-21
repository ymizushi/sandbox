extern crate gtk;
extern crate gio;

use gtk::{ WidgetExt, WindowExt };
use gio::ApplicationExt;

fn main() {
    match gtk::Application::new("ymizushi.svg-min-engine", gio::APPLICATION_HANDLES_OPEN) {
        Ok(app) => {
            app.connect_activate(|app| {
                let win = gtk::ApplicationWindow::new(&app);
                win.set_title("svg-min-engine");
                win.show_all();
            });

            app.run(&[""]);
        },
        Err(_) => {
            println!("Application start up error");
        }
    };
}
