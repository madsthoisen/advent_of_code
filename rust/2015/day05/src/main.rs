use std::fs;

fn n_vowels(s: &str) -> u8 {
    let list_of_vowels = vec!['a', 'e', 'i', 'o', 'u'];
    let mut count: u8 = 0;
    for ch in s.chars() {
        if list_of_vowels.contains(&ch) {
            count += 1
        }
    }
    count
}

fn twice_in_a_row(s: &str) -> bool {
    let mut prev: char = '$';
    for ch in s.chars() {
        if ch == prev {
            return true;
        }
        prev = ch;
    }
    return false;
}

fn has_illegal_pair(s: &str) -> bool {
    let illegal_pairs = vec!["ab", "cd", "pq", "xy"];
    for i in 0..s.len() - 1 {
        let pair = s.get(i..i + 2).expect("");
        if illegal_pairs.contains(&pair) {
            return true;
        }
    }
    return false;
}

fn has_two_pairs(s: &str) -> bool {
    for i in 0..s.len() - 1 {
        let pair = s.get(i..i + 2).expect("");
        if s[i + 2..].contains(pair) {
            return true;
        }
    }
    return false;
}

fn has_repeat_with_whitespace(s: &str) -> bool {
    for i in 0..s.len() - 1 {
        if s.chars().nth(i) == s.chars().nth(i + 2) {
            return true;
        }
    }
    return false;
}

fn is_nice_part_1(s: &str) -> bool {
    if n_vowels(&s) < 3 {
        return false;
    }
    if !twice_in_a_row(&s) {
        return false;
    }
    if has_illegal_pair(&s) {
        return false;
    }
    return true;
}

fn is_nice_part_2(s: &str) -> bool {
    if !has_two_pairs(&s) {
        return false;
    }
    if !has_repeat_with_whitespace(&s) {
        return false;
    }
    return true;
}

fn part_1(strings: &str) {
    let mut n_nice_strings: u32 = 0;
    for s in strings.split('\n') {
        if is_nice_part_1(s) {
            n_nice_strings += 1;
        }
    }
    println!("part 1: {n_nice_strings}");
}

fn part_2(strings: &str) {
    let mut n_nice_strings: u32 = 0;
    for s in strings.split('\n') {
        if is_nice_part_2(s) {
            n_nice_strings += 1;
        }
    }
    println!("part 2: {n_nice_strings}");
}

fn main() {
    let strings = fs::read_to_string("../input").expect("");
    let strings = strings.trim();
    part_1(&strings);
    part_2(&strings);
}
