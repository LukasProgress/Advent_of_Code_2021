
createBitSum :: [[Double]] -> [Double]
createBitSum xs = sumUp xs
    where   sumUp ([]:_) = []
            sumUp xs = foldr (\a b -> head a + b) 0 xs : sumUp (map tail xs)

averageBits :: [[Double]] -> Double -> [Double]
averageBits xs len = map (/ len) (createBitSum xs)

wholeBits :: [Double] -> [Int]
wholeBits = map round

wholeBitsUp :: [Double] -> [Int]
wholeBitsUp [] = []
wholeBitsUp (0.5:xs) = 1 : wholeBitsUp xs
wholeBitsUp (x:xs)  = round x : wholeBitsUp xs


invert :: [Int] -> [Int]
invert [] = []
invert (1:xs) = 0 : invert xs
invert (0:xs) = 1: invert xs

getNumber :: [Int] -> Int
getNumber [] = 0
getNumber (x:xs) = x + 2 * getNumber xs

------

getOxygenRating :: [[Double]] -> [Int] -> Int -> [Int]
getOxygenRating ([]:_) _ _ = []
getOxygenRating [xs] _ _ = map round xs
getOxygenRating xs bits runde  = getOxygenRating newBitList (wholeBitsUp (averageBits newBitList (fromIntegral (length newBitList)))) (runde + 1)
    where newBitList = filter (\x -> round (x!!runde)  == bits!!runde) xs


getCO2Rating :: [[Double]] -> [Int] -> Int -> [Int]
getCO2Rating ([]:_) _ _ = []
getCO2Rating [xs] _ _ = map round xs
getCO2Rating xs bits runde  = getCO2Rating newBitList (wholeBitsUp (averageBits newBitList (fromIntegral (length newBitList)))) (runde + 1)
    where newBitList = filter (\x -> round (x!!runde)  /= bits!!runde) xs
                                                


main :: IO()
main = do
    content <- readFile "Data.txt"
    let dataIn = (map.map) (read . pure ::Char->Double) (lines content)
    let dataLength = fromInteger (toInteger (length dataIn)) :: Double
    let gamma = wholeBits (averageBits dataIn dataLength)
    let epsilon = invert gamma
    let result1 = getNumber (reverse epsilon) * getNumber (reverse gamma)
    print result1
    -- gamma shows which rows have mostly ones or zeroes in the whole data
    let ox = getOxygenRating dataIn gamma 0
    let co = getCO2Rating dataIn gamma 0
    let testData = [[0,0,1,0,0],[1,1,1,1,0],[1,0,1,1,0],[1,0,1,1,1],[1,0,1,0,1],[0,1,1,1,1],[0,0,1,1,1],[1,1,1,0,0],[1,0,0,0,0],[1,1,0,0,1],[0,0,0,1,0],[0,1,0,1,0]]
    let testGamma = wholeBits (averageBits testData (fromInteger (toInteger (length testData)) :: Double))
    let testEpsilon = invert testGamma
    --print testGamma
    --print $ getOxygenRating testData testGamma 0
    --print $ getCO2Rating testData testGamma 0
    print ox
    print co
    print $ getNumber (reverse ox) * getNumber (reverse co)
