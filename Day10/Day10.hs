import Data.List

part1 :: [String] -> Int
part1 [] = 0
part1 (x:xs) = check x [] + part1 xs

check :: [Char] -> [Char] -> Int
check [] _ = 0
check ('(':xs) ys = check xs (')' : ys)
check ('[':xs) ys = check xs (']' : ys)
check ('{':xs) ys = check xs ('}' : ys)
check ('<':xs) ys = check xs ('>' : ys)
check (x:xs) (y:ys) | x == y = check xs ys
                    | x == ')' = 3
                    | x == ']' = 57
                    | x == '}' = 1197
                    | x == '>' = 25137
check _ _ = 0


part2 :: [String] -> Int
part2 lines = getMiddle (sort (getCompletionStringNumbers lines))

getCompletionStringNumbers :: [String] -> [Int]
getCompletionStringNumbers lines = map (\l -> check2 l [] 0) (filter (\l -> check l [] == 0) lines)

-- InputList -> RestList -> accumulator -> result
check2 :: [Char] -> [Char] -> Int -> Int
check2 [] [] acc = acc
check2 [] (')':xs) acc = check2 [] xs (5 * acc + 1)
check2 [] (']':xs) acc = check2 [] xs (5 * acc + 2)
check2 [] ('}':xs) acc = check2 [] xs (5 * acc + 3)
check2 [] ('>':xs) acc = check2 [] xs (5 * acc + 4)
check2 ('(':xs) ys acc = check2 xs (')' : ys) acc
check2 ('[':xs) ys acc = check2 xs (']' : ys) acc
check2 ('{':xs) ys acc = check2 xs ('}' : ys) acc
check2 ('<':xs) ys acc = check2 xs ('>' : ys) acc
check2 (x:xs) (y:ys) acc | x == y = check2 xs ys acc

getMiddle :: [Int] -> Int
getMiddle xs = xs!!(length xs `div` 2)


main :: IO ()
main = do
    content <- readFile "Data.txt"
    let dataIn = (lines content)
    print $ part1 dataIn
    print $ part2 dataIn
