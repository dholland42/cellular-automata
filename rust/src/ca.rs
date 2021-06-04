/// Functions for evolving cellular automata.

use std::collections::HashMap;
use itertools;

/// Convert an unsigned integer to binary.
fn to_bin(num: u32) -> Vec<u32> {
    let formatted = format!("{:b}", num);
    let chars: Vec<u32> = formatted.chars().map(|c| c.to_digit(10).unwrap()).collect();
    return chars
}

/// Return all possible combinations of 3 consecutive cells.
fn get_rules() -> Vec<(u32, u32, u32)> {
    let options = itertools::iproduct!(0..2, 0..2, 0..2);
    let options: Vec<(u32, u32, u32)> = options.collect();
    return options
}

/// Return a mapping from 3-cell state to single state for
/// a given rule id.
fn get_mapping(rule_id: u32) -> HashMap<(u32, u32, u32), u32> {
    let vals = to_bin(rule_id);
    let rules = get_rules();
    let mut stuff: Vec<((u32, u32, u32), u32)> = Vec::new();
    for item in rules.iter().zip(vals.iter()) {
        stuff.push((*item.0, *item.1))
    };
    let mapping: HashMap<_, _> = stuff.into_iter().collect();
    return mapping
}

/// Evolve a full set of cells according to a rule id.
pub fn evolve(state: Vec<u32>, rule_id: u32) -> Vec<u32> {
    let len = state.len();
    let mapping = get_mapping(rule_id);
    let mut newstate: Vec<u32> = Vec::new();
    for i in 0..len {
        let v0: u32 = if i as i32 - 1 < 0 {0} else {state[i-1] as u32};
        let v1 = state[i] as u32;
        let v2: u32 = if i  + 1 == len {0} else {state[i+1] as u32};
        let newval = match mapping.get(&(v0, v1, v2)) {Some(item) => item, None => &0};
        newstate.push(*newval);
    }
    newstate
}