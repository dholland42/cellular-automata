// Data models

use serde::{Serialize, Deserialize};

#[derive(Serialize, Deserialize, Debug)]
pub struct State {
    pub state: Vec<u32>,
    pub rule: u32,
}
