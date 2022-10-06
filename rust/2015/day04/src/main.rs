use md5;

fn get_md5_hash(s: &str) {
    let mut i: u32 = 1;
    let mut part_1_found = false;
    loop {
        let tmp_string = format!("{}{i}", s);
        let digest = md5::compute(tmp_string);
        let digest_string = format!("{:?}", digest);
        let x: Vec<char> = digest_string.chars().collect();
        if &x[0..5] == ['0'; 5] && !part_1_found{
            println!("part 1: {}", i);
            part_1_found = true;
        }
        if &x[0..6] == ['0'; 6] {
            println!("part 2: {}", i);
            break;
        }
        i += 1;
    }

}


fn main() {
    let input_str: &str = "bgvyzdsv";
    get_md5_hash(input_str);
}
