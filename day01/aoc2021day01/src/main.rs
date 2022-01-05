fn main() {
    use std::fs::File;
    use std::io::prelude::*;
    use std::path::Path;

    let test_input = "199
200
208
210
200
207
240
269
260
263";
    let answer = part_1(test_input);
    assert_eq!(answer, 7);

    let path = Path::new("../input.txt");
    let display = path.display();

    // Open the path in read-only mode, returns `io::Result<File>`
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };
    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => {
            let answer_part_1 = part_1(&s);
            println!("The answer is {}", answer_part_1);
        }
    }
}

fn part_1(input: &str) -> i32 {
    use std::cmp::Ordering;
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
    return answer;
}
