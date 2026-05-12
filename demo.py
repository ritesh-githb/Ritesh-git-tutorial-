print("Start small. Ship something.")
print('Hello brother')
print('heloo sunny',1,'what happens')
print('hello sunny',12,'good things',sep='$') ## comma separator delimiter 

## for print with multiline 
## prinnt("Hello ritesh patil. what is the issue you are 
## facing") ## SyntaxError: unterminated string literal (detected at line 7)

print("""Hello 'ritesh' patil. what is the issue you are? 
facing""") ## SyntaxError: unterminated string literal (detected at line 7) 
## we need to tackle escape character because we need to know what is the starting and ending point.

print("Hello 'ritesh' patil. what is the issue you are")
## backslash is escaping the character 
print("Hello \'ritesh\' patil. what is the issue you are")
