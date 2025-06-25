#Rupali Kakadia and Yeon Soo Choi


#Data preparation
#Open customer feedback file and word sentiment file
try:
    with open('customer_feedback.txt','r') as f:
        data = f.read()
except Exception as e:
    print(f'An error occured: {e}')
try:
    with open('word_sentiment.txt','r') as f:
        data2 = f.read()
except Exception as e:
    print(f'An error occured: {e}')

#Data analysis
#Calculate and display total number of feedback
feedback = data.split('\n') [1:101]
print(feedback)
total_number_feedback = len(feedback)
print("Total number feedback : ", total_number_feedback)

#Determine the average word count per feedback entries
sum_word = 0

for entry in feedback:
    word_count = len(entry.split()[1:])
    sum_word += word_count

average_word_count = sum_word / total_number_feedback
print("Average word count : ",average_word_count)

#Classify the sentiment for each feedback
positive = []
negative = []
neutral = []

sentiment = data2.splitlines()
print(sentiment)
present_section = None

for section in sentiment:
    if '**Positive Words:**' in section:
        present_section = 'positive'
    elif '**Negative Words:**' in section:
        present_section = 'negative'
    elif '**Neutral Words:**' in section:
        present_section = 'neutral'
    elif section.startswith('-'):
        sentiment_word = section.strip('- ').strip()
        if present_section == 'positive':
            positive.append(sentiment_word)
        elif present_section == 'negative':
            negative.append(sentiment_word)
        elif present_section == 'neutral':
            neutral.append(sentiment_word)

print("Positive Words: ", positive)
print("Negative Words: ", negative)
print("Neutral Words: ", neutral)

#Identify the most commom keywords in the feedback
positive_word_count = {}
negative_word_count = {}

for keyword in feedback:
    words = keyword.lower().split()

    for w in words:
        if w in positive:
            if w in positive_word_count:
                positive_word_count[w] += 1
            else:
                positive_word_count[w] = 1

        elif w in negative:
            if w in negative_word_count:
                negative_word_count[w] += 1
            else:
                negative_word_count[w] = 1

sort_p = sorted(positive_word_count.items(), key=lambda item: item[1], reverse = True)
sort_n = sorted(negative_word_count.items(), key=lambda item: item[1], reverse = True)

common_positive = sort_p[:1]
common_negative =sort_n[:1]

for k,v in common_positive:
    print(f"Most common positive keyword: {k}, The count: {v}")

for k,v in common_negative:
    print(f"Most common negative keyword: {k}, The count: {v}")

#Calculate the overall sentiment distribution
positive_count = 0
neutral_count = 0
negative_count = 0

for f in feedback:
    f_words = f.lower().split()
    f_positive = any(word in positive for word in f_words)
    f_negative = any(word in negative for word in f_words)
    f_neutral = any(word in neutral for word in f_words)

    if f_positive:
        positive_count += 1
    elif f_negative:
        negative_count += 1
    elif f_neutral:
        neutral_count += 1

positive_percentage = (positive_count / total_number_feedback) * 100
negative_percentage = (negative_count / total_number_feedback) * 100
neutral_percentage = (neutral_count / total_number_feedback) * 100

print(f'Distribution of Positive keywords: {int(positive_percentage)}%')
print(f'Distribution of Negative keywords: {int(negative_percentage)}%')
print(f'Distribution of Neutral keywords: {int(neutral_percentage)}%')

#Data reporting
try:
    with open('feedback_summary.txt','w') as f:
        f.write(f'Total number of feedback entries: {total_number_feedback}')
        f.write(f'\nCommon positive keywords and count: {common_positive}')
        f.write(f'\nCommon negative keywords and count: {common_negative}')
        f.write(f'\nAverage word count per feedback entry: {average_word_count}')
        f.write(f'\nSentiment Distribution: ')
        f.write(f'\nPositive: {int(positive_percentage)}%')
        f.write(f'\nNegative: {int(negative_percentage)}%')
        f.write(f'\nNetural: {int(neutral_percentage)}%')
except Exception as e:
    print(f'An error occured: {e}')

#Visualize the sentiment distribution using simple text-based charts

def chart(sentiment, count, total):
    text_chart = f"{sentiment}:" + '*' * int((count/total)*100)
    return text_chart

print(chart('Distribution of Positive keywords', positive_count, total_number_feedback))
print(chart('Distribution of Negative keywords', negative_count, total_number_feedback))
print(chart('Distribution of Neutral keywords', neutral_count, total_number_feedback))

