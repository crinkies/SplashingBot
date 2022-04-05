SetMouseDelay -1
SetDefaultMouseSpeed, 0
Loop
{
    CoordMode, Pixel, window
    PixelSearch, FoundX, FoundY, 6, 29, 1559, 1016, 0xFFB700, 0, Fast RGB
}
Until ErrorLevel = 0
random, rand, 0, 5
random, rand2, 0, 10
MouseMove, FoundX+rand, FoundY+rand2
click
ExitApp
