// Just a simple starting point where we evolve
// an initial state 10 times accordint to rule 32

mod ca;

fn main() {
    // set up our initial state
    let mut state: Vec<u32> = Vec::new() ;
    state.extend([0, 0, 0, 1, 0, 0, 0, 0].iter().copied());
    // evolve 10 times and print to stdout
    println!("{:?}", state);
    for _ in 0..10 {
        state = ca::evolve(state, 32);
        println!("{:?}", state);
    }
}
