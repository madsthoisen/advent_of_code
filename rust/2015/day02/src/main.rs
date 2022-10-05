use std::fs;

fn calculate_wrapping_paper(s: [i32; 3]) -> i32 {
    let mut output: i32 = 0;
    let areas: [i32; 3] = [s[0] * s[1], s[1] * s[2], s[0] * s[2]];
    match areas.iter().min() {
        Some(x) => output += *x,
        None => println!("no min found for {:?}", areas),
    }
    let sum: i32 = areas.iter().sum();
    output + 2 * sum
}

fn calculate_ribbon(s: [i32; 3]) -> i32 {
    let mut cs = s;
    cs.sort();
    2 * (cs[0] + cs[1]) + cs[0] * cs[1] * cs[2]
}

fn go_through_gifts(s: &str) -> (i32, i32) {
    let mut part_1: i32 = 0;
    let mut part_2: i32 = 0;
    for line in s.split("\n") {
        let mut sides: [i32; 3] = [0; 3];
        for item in line.split('x').enumerate() {
            let (i, x): (usize, &str) = item;
            let val: i32 = x.parse().unwrap();
            sides[i] = val;
        }
        let paper: i32 = calculate_wrapping_paper(sides);
        let ribbon: i32 = calculate_ribbon(sides);
        part_1 += paper;
        part_2 += ribbon;
    }
    (part_1, part_2)
}

fn main() {
    let s = fs::read_to_string("../input").expect("");
    let (p1, p2) = go_through_gifts(&s.trim());
    println!("part 1: {}", p1);
    println!("part 2: {}", p2);
}
