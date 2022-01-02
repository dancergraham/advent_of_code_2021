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
    let lines = input.lines();
    for line in lines {
        let order = line.cmp(line0);
        if order == Ordering::Greater {
            answer = answer + 1;
        }
        line0 = line;
    }
    println!("The answer is {}", answer)
}
