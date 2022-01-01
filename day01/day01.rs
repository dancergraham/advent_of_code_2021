#![allow(unused)]
fn main() {
    use std::cmp::Ordering;
    let input = "199
200
208
210
200
207
240
269
260
263";
    let mut line0 = "9999";
    let mut answer = 0;
    let mut lines = input.lines();
    for mut line in lines {
        let mut order = line.cmp(line0);
        if order == Ordering::Greater {
            answer = answer + 1;
        }
        line0 = line;
    }
    println!("The answer is {}", answer)
}
