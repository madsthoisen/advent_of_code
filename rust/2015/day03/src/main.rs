use std::collections::HashSet;
use std::fs;

fn solve(s: &str) -> (usize, usize) {
    let mut positions = HashSet::new();
    let mut positions_combined = HashSet::new();

    let mut pos: [i32; 2] = [0, 0];
    let mut pos_santa: [i32; 2] = [0, 0];
    let mut pos_robot: [i32; 2] = [0, 0];

    positions.insert(pos);
    positions_combined.insert(pos);

    for item in s.chars().enumerate() {
        let (i, ch) = item;
        let (coord, val) = match ch {
            '<' => (0, -1),
            '>' => (0, 1),
            '^' => (1, -1),
            'v' => (1, 1),
            _ => (0, 0),
        };
        pos[coord] += val;
        positions.insert(pos);
        if i % 2 == 0 {
            pos_santa[coord] += val;
            positions_combined.insert(pos_santa);
        } else if i % 2 == 1 {
            pos_robot[coord] += val;
            positions_combined.insert(pos_robot);
        }
    }
    let part_1 = positions.len();
    let part_2 = positions_combined.len();
    (part_1, part_2)
}

fn main() {
    let s = fs::read_to_string("../input").expect("");
    let (p1, p2) = solve(&s.trim());
    println!("part 1: {}", p1);
    println!("part 2: {}", p2);
}
