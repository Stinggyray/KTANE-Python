# Color Flash / Colour Flash

Will flash a sequence of 8 words that represent colors in different colors.

Colors / words: Red, Yellow, Green, Blue, Magenta, White

## Rules
Depending on the color of the last word, follow these rules.

### Red
| Rule | Press | When |
| --- | --- | --- |
| Green is the word 3+ times | Yes | 3rd time Green is used as either word/color in sequence |
| Blue is the color exactly 1 time | No | On the word Magenta |
| Else | Yes | Last time White is the word/color |

### Yellow
| Rule | Press | When |
| --- | --- | --- |
| The word Blue is shown in green | Yes | First time green is the color |
| The word White is shown in white/red | Yes | 2nd time in sequence the color of the word doesn't match the word itself |
| Else | No | Count the # of times Magenta is the word/color - press No on that number in the sequence |

### Green
| Rule | Press | When |
| --- | --- | --- |
| A word occurs twice in a row with different colors | No | 5th entry in sequence |
| Magenta is the word 3+ times | No | 1st time Yellow is the word/color |
| Else | Yes | Any position where the color matches the word |

### Blue
| Rule | Press | When |
| --- | --- | --- |
| Color does not match word 3+ times | Yes | First time color does not match word |
| Red in yellow color / Yellow in white color | No | White in red color |
| Else | Yes | The last time Green is the word/color |

### Magenta
| Rule | Press | When |
| --- | --- | --- |
| A color occurs twice in a row with different words | Yes | 3rd entry in sequence |
| The word Yellow appears more times than the color blue | No | Last time Yellow is the word |
| Else | No | First time when the color matches the word of the 7th entry in sequence |

### White
| Rule | Press | When |
| --- | --- | --- |
| 3rd color matches 4th/5th word | No | First time Blue is the word/color |
| Yellow in red color | Yes | Last time blue is the color |
| Else | No | Anytime |