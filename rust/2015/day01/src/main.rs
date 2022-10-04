use std::fs;

fn solve(s: &str) -> (i64, i64){
    let mut count: i64 = 0;
    let mut position: i64 = 1;
    let mut part_2: bool = false;
    for x in s.chars() {
        if x == '(' {
            count += 1;
            }
        else if x == ')' {
            count -= 1
            }
        if count == -1 && !part_2{
            part_2 = true;
            }
        if !part_2{
            position += 1;
            }
        }
    (count, position)
    }

fn main() {
    let s = fs::read_to_string("../input").expect("");
    let (p1, p2) = solve(&s);
    println!("part 1: {}", p1);
    println!("part 2: {}", p2);
}
