import urllib

first_review_url = "http://www.amazon.com/product-reviews/"
middle_review_url = "/ref=cm_cr_pr_top_link_next_2?ie=UTF8&filterBy=addFiveStar&pageNumber="
last_review_url = "&showViewpoints=0&sortBy=bySubmissionDateDescending"


check_list = {
'first birthday':1,
'1st birthday':1,
'1 y.o':1,
'1 y.o.':1,
'1 y/o':1,
'1 year old':1,
'1 years old':1,
'1 yo':1,
'1 yr ol':1,
'1 yr old':1,
'1 yrs ol':1,
'1 yrs old':1,
'1-year-old':1,
'Grandchildren ages 1':1,
'boys ( 1':1,
'boys( 1':1,
'daughters ( 1':1,
'daughters( 1':1,
'girls ( 1':1,
'girls( 1':1,
'grandchildren ( 1':1,
'grandchildren( 1':1,
'granddaughters ( 1':1,
'granddaughters( 1':1,
'grandkids ( 1':1,
'grandkids( 1':1,
'grandsons ( 1':1,
'grandsons( 1':1,
'he just turned 1':1,
'he was 1':1,
'is almost 1':1,
'kids ( 1':1,
'kids( 1':1,
'sons ( 1':1,
'sons( 1':1,
'they are 1':1,
'when he turned 1':1,
'when he was 1':1,
'one y/o':1,
'one year old':1,
'one years old':1,
'one yo':1,
'one yr ol':1,
'one yr old':1,
'one yrs ol':1,
'one yrs old':1,
'one-year-old':1,
'Grandchildren ages one':1,
'boys (one':1,
'boys(one':1,
'daughters (one':1,
'daughters(one':1,
'girls (one':1,
'girls(one':1,
'grandchildren (one':1,
'grandchildren(one':1,
'granddaughters (one':1,
'granddaughters(one':1,
'grandkids (one':1,
'grandkids(one':1,
'grandsons ( one':1,
'grandsons( one':1,
'he just turned one':1,
'he was one':1,
'is almost one':1,
'kids ( one':1,
'kids( one':1,
'sons ( one':1,
'sons( one':1,
'they are one':1,
'when he turned one':1,
'when he was one':1,
'second birthday':2,
'2nd birthday':2,
'2 y.o':2,
'2 y.o.':2,
'2 y/o':2,
'2 year old':2,
'2 years old':2,
'2 yo':2,
'2 yr ol':2,
'2 yr old':2,
'2 yrs ol':2,
'2 yrs old':2,
'2-year-old':2,
'Grandchildren ages 2':2,
'boys ( 2':2,
'boys( 2':2,
'daughters ( 2':2,
'daughters( 2':2,
'girls ( 2':2,
'girls( 2':2,
'grandchildren ( 2':2,
'grandchildren( 2':2,
'granddaughters ( 2':2,
'granddaughters( 2':2,
'grandkids ( 2':2,
'grandkids( 2':2,
'grandsons ( 2':2,
'grandsons( 2':2,
'he just turned 2':2,
'he was 2':2,
'is almost 2':2,
'kids ( 2':2,
'kids( 2':2,
'sons ( 2':2,
'sons( 2':2,
'they are 2':2,
'when he turned 2':2,
'when he was 2':2,
'two y/o':2,
'two year old':2,
'two years old':2,
'two yo':2,
'two yr ol':2,
'two yr old':2,
'two yrs ol':2,
'two yrs old':2,
'two-year-old':2,
'Grandchildren ages two':2,
'boys (two':2,
'boys(two':2,
'daughters (two':2,
'daughters(two':2,
'girls (two':2,
'girls(two':2,
'grandchildren (two':2,
'grandchildren(two':2,
'granddaughters (two':2,
'granddaughters(two':2,
'grandkids (two':2,
'grandkids(two':2,
'grandsons ( two':2,
'grandsons( two':2,
'he just turned two':2,
'he was two':2,
'is almost two':2,
'kids ( two':2,
'kids( two':2,
'sons ( two':2,
'sons( two':2,
'they are two':2,
'when he turned two':2,
'when he was two':2,
'third birthday':3,
'3rd birthday':3,
'3 y.o':3,
'3 y.o.':3,
'3 y/o':3,
'3 year old':3,
'3 years old':3,
'3 yo':3,
'3 yr ol':3,
'3 yr old':3,
'3 yrs ol':3,
'3 yrs old':3,
'3-year-old':3,
'Grandchildren ages 3':3,
'boys ( 3':3,
'boys( 3':3,
'daughters ( 3':3,
'daughters( 3':3,
'girls ( 3':3,
'girls( 3':3,
'grandchildren ( 3':3,
'grandchildren( 3':3,
'granddaughters ( 3':3,
'granddaughters( 3':3,
'grandkids ( 3':3,
'grandkids( 3':3,
'grandsons ( 3':3,
'grandsons( 3':3,
'he just turned 3':3,
'he was 3':3,
'is almost 3':3,
'kids ( 3':3,
'kids( 3':3,
'sons ( 3':3,
'sons( 3':3,
'they are 3':3,
'when he turned 3':3,
'when he was 3':3,
'three y/o':3,
'three year old':3,
'three years old':3,
'three yo':3,
'three yr ol':3,
'three yr old':3,
'three yrs ol':3,
'three yrs old':3,
'three-year-old':3,
'Grandchildren ages three':3,
'boys (three':3,
'boys(three':3,
'daughters (three':3,
'daughters(three':3,
'girls (three':3,
'girls(three':3,
'grandchildren (three':3,
'grandchildren(three':3,
'granddaughters (three':3,
'granddaughters(three':3,
'grandkids (three':3,
'grandkids(three':3,
'grandsons ( three':3,
'grandsons( three':3,
'he just turned three':3,
'he was three':3,
'is almost three':3,
'kids ( three':3,
'kids( three':3,
'sons ( three':3,
'sons( three':3,
'they are three':3,
'when he turned three':3,
'when he was three':3,
'fourth birthday':4,
'4th birthday':4,
'4 y.o':4,
'4 y.o.':4,
'4 y/o':4,
'4 year old':4,
'4 years old':4,
'4 yo':4,
'4 yr ol':4,
'4 yr old':4,
'4 yrs ol':4,
'4 yrs old':4,
'4-year-old':4,
'Grandchildren ages 4':4,
'boys ( 4':4,
'boys( 4':4,
'daughters ( 4':4,
'daughters( 4':4,
'girls ( 4':4,
'girls( 4':4,
'grandchildren ( 4':4,
'grandchildren( 4':4,
'granddaughters ( 4':4,
'granddaughters( 4':4,
'grandkids ( 4':4,
'grandkids( 4':4,
'grandsons ( 4':4,
'grandsons( 4':4,
'he just turned 4':4,
'he was 4':4,
'is almost 4':4,
'kids ( 4':4,
'kids( 4':4,
'sons ( 4':4,
'sons( 4':4,
'they are 4':4,
'when he turned 4':4,
'when he was 4':4,
'four y/o':4,
'four year old':4,
'four years old':4,
'four yo':4,
'four yr ol':4,
'four yr old':4,
'four yrs ol':4,
'four yrs old':4,
'four-year-old':4,
'Grandchildren ages four':4,
'boys (four':4,
'boys(four':4,
'daughters (four':4,
'daughters(four':4,
'girls (four':4,
'girls(four':4,
'grandchildren (four':4,
'grandchildren(four':4,
'granddaughters (four':4,
'granddaughters(four':4,
'grandkids (four':4,
'grandkids(four':4,
'grandsons ( four':4,
'grandsons( four':4,
'he just turned four':4,
'he was four':4,
'is almost four':4,
'kids ( four':4,
'kids( four':4,
'sons ( four':4,
'sons( four':4,
'they are four':4,
'when he turned four':4,
'when he was four':4,
'fifth birthday':5,
'5th birthday':5,
'5 y.o':5,
'5 y.o.':5,
'5 y/o':5,
'5 year old':5,
'5 years old':5,
'5 yo':5,
'5 yr ol':5,
'5 yr old':5,
'5 yrs ol':5,
'5 yrs old':5,
'5-year-old':5,
'Grandchildren ages 5':5,
'boys ( 5':5,
'boys( 5':5,
'daughters ( 5':5,
'daughters( 5':5,
'girls ( 5':5,
'girls( 5':5,
'grandchildren ( 5':5,
'grandchildren( 5':5,
'granddaughters ( 5':5,
'granddaughters( 5':5,
'grandkids ( 5':5,
'grandkids( 5':5,
'grandsons ( 5':5,
'grandsons( 5':5,
'he just turned 5':5,
'he was 5':5,
'is almost 5':5,
'kids ( 5':5,
'kids( 5':5,
'sons ( 5':5,
'sons( 5':5,
'they are 5':5,
'when he turned 5':5,
'when he was 5':5,
'five y/o':5,
'five year old':5,
'five years old':5,
'five yo':5,
'five yr ol':5,
'five yr old':5,
'five yrs ol':5,
'five yrs old':5,
'five-year-old':5,
'Grandchildren ages five':5,
'boys (five':5,
'boys(five':5,
'daughters (five':5,
'daughters(five':5,
'girls (five':5,
'girls(five':5,
'grandchildren (five':5,
'grandchildren(five':5,
'granddaughters (five':5,
'granddaughters(five':5,
'grandkids (five':5,
'grandkids(five':5,
'grandsons ( five':5,
'grandsons( five':5,
'he just turned five':5,
'he was five':5,
'is almost five':5,
'kids ( five':5,
'kids( five':5,
'sons ( five':5,
'sons( five':5,
'they are five':5,
'when he turned five':5,
'when he was five':5,
'sixth birthday':6,
'6th birthday':6,
'6 y.o':6,
'6 y.o.':6,
'6 y/o':6,
'6 year old':6,
'6 years old':6,
'6 yo':6,
'6 yr ol':6,
'6 yr old':6,
'6 yrs ol':6,
'6 yrs old':6,
'6-year-old':6,
'Grandchildren ages 6':6,
'boys ( 6':6,
'boys( 6':6,
'daughters ( 6':6,
'daughters( 6':6,
'girls ( 6':6,
'girls( 6':6,
'grandchildren ( 6':6,
'grandchildren( 6':6,
'granddaughters ( 6':6,
'granddaughters( 6':6,
'grandkids ( 6':6,
'grandkids( 6':6,
'grandsons ( 6':6,
'grandsons( 6':6,
'he just turned 6':6,
'he was 6':6,
'is almost 6':6,
'kids ( 6':6,
'kids( 6':6,
'sons ( 6':6,
'sons( 6':6,
'they are 6':6,
'when he turned 6':6,
'when he was 6':6,
'sixth y/o':6,
'sixth year old':6,
'sixth years old':6,
'sixth yo':6,
'sixth yr ol':6,
'sixth yr old':6,
'sixth yrs ol':6,
'sixth yrs old':6,
'sixth-year-old':6,
'Grandchildren ages sixth':6,
'boys (sixth':6,
'boys(sixth':6,
'daughters (sixth':6,
'daughters(sixth':6,
'girls (sixth':6,
'girls(sixth':6,
'grandchildren (sixth':6,
'grandchildren(sixth':6,
'granddaughters (sixth':6,
'granddaughters(sixth':6,
'grandkids (sixth':6,
'grandkids(sixth':6,
'grandsons ( sixth':6,
'grandsons( sixth':6,
'he just turned sixth':6,
'he was sixth':6,
'is almost sixth':6,
'kids ( sixth':6,
'kids( sixth':6,
'sons ( sixth':6,
'sons( sixth':6,
'they are sixth':6,
'when he turned sixth':6,
'when he was sixth':6,
'seventh birthday':7,
'7th birthday':7,
'7 y.o':7,
'7 y.o.':7,
'7 y/o':7,
'7 year old':7,
'7 years old':7,
'7 yo':7,
'7 yr ol':7,
'7 yr old':7,
'7 yrs ol':7,
'7 yrs old':7,
'7-year-old':7,
'Grandchildren ages 7':7,
'boys ( 7':7,
'boys( 7':7,
'daughters ( 7':7,
'daughters( 7':7,
'girls ( 7':7,
'girls( 7':7,
'grandchildren ( 7':7,
'grandchildren( 7':7,
'granddaughters ( 7':7,
'granddaughters( 7':7,
'grandkids ( 7':7,
'grandkids( 7':7,
'grandsons ( 7':7,
'grandsons( 7':7,
'he just turned 7':7,
'he was 7':7,
'is almost 7':7,
'kids ( 7':7,
'kids( 7':7,
'sons ( 7':7,
'sons( 7':7,
'they are 7':7,
'when he turned 7':7,
'when he was 7':7,
'seven y/o':7,
'seven year old':7,
'seven years old':7,
'seven yo':7,
'seven yr ol':7,
'seven yr old':7,
'seven yrs ol':7,
'seven yrs old':7,
'seven-year-old':7,
'Grandchildren ages seven':7,
'boys (seven':7,
'boys(seven':7,
'daughters (seven':7,
'daughters(seven':7,
'girls (seven':7,
'girls(seven':7,
'grandchildren (seven':7,
'grandchildren(seven':7,
'granddaughters (seven':7,
'granddaughters(seven':7,
'grandkids (seven':7,
'grandkids(seven':7,
'grandsons ( seven':7,
'grandsons( seven':7,
'he just turned seven':7,
'he was seven':7,
'is almost seven':7,
'kids ( seven':7,
'kids( seven':7,
'sons ( seven':7,
'sons( seven':7,
'they are seven':7,
'when he turned seven':7,
'when he was seven':7,
'eighth birthday':8,
'8th birthday':8,
'8 y.o':8,
'8 y.o.':8,
'8 y/o':8,
'8 year old':8,
'8 years old':8,
'8 yo':8,
'8 yr ol':8,
'8 yr old':8,
'8 yrs ol':8,
'8 yrs old':8,
'8-year-old':8,
'Grandchildren ages 8':8,
'boys ( 8':8,
'boys( 8':8,
'daughters ( 8':8,
'daughters( 8':8,
'girls ( 8':8,
'girls( 8':8,
'grandchildren ( 8':8,
'grandchildren( 8':8,
'granddaughters ( 8':8,
'granddaughters( 8':8,
'grandkids ( 8':8,
'grandkids( 8':8,
'grandsons ( 8':8,
'grandsons( 8':8,
'he just turned 8':8,
'he was 8':8,
'is almost 8':8,
'kids ( 8':8,
'kids( 8':8,
'sons ( 8':8,
'sons( 8':8,
'they are 8':8,
'when he turned 8':8,
'when he was 8':8,
'eight y/o':8,
'eight year old':8,
'eight years old':8,
'eight yo':8,
'eight yr ol':8,
'eight yr old':8,
'eight yrs ol':8,
'eight yrs old':8,
'eight-year-old':8,
'Grandchildren ages eight':8,
'boys (eight':8,
'boys(eight':8,
'daughters (eight':8,
'daughters(eight':8,
'girls (eight':8,
'girls(eight':8,
'grandchildren (eight':8,
'grandchildren(eight':8,
'granddaughters (eight':8,
'granddaughters(eight':8,
'grandkids (eight':8,
'grandkids(eight':8,
'grandsons ( eight':8,
'grandsons( eight':8,
'he just turned eight':8,
'he was eight':8,
'is almost eight':8,
'kids ( eight':8,
'kids( eight':8,
'sons ( eight':8,
'sons( eight':8,
'they are eight':8,
'when he turned eight':8,
'when he was eight':8,
'ninth birthday':9,
'9th birthday':9,
'9 y.o':9,
'9 y.o.':9,
'9 y/o':9,
'9 year old':9,
'9 years old':9,
'9 yo':9,
'9 yr ol':9,
'9 yr old':9,
'9 yrs ol':9,
'9 yrs old':9,
'9-year-old':9,
'Grandchildren ages 9':9,
'boys ( 9':9,
'boys( 9':9,
'daughters ( 9':9,
'daughters( 9':9,
'girls ( 9':9,
'girls( 9':9,
'grandchildren ( 9':9,
'grandchildren( 9':9,
'granddaughters ( 9':9,
'granddaughters( 9':9,
'grandkids ( 9':9,
'grandkids( 9':9,
'grandsons ( 9':9,
'grandsons( 9':9,
'he just turned 9':9,
'he was 9':9,
'is almost 9':9,
'kids ( 9':9,
'kids( 9':9,
'sons ( 9':9,
'sons( 9':9,
'they are 9':9,
'when he turned 9':9,
'when he was 9':9,
'nine y/o':9,
'nine year old':9,
'nine years old':9,
'nine yo':9,
'nine yr ol':9,
'nine yr old':9,
'nine yrs ol':9,
'nine yrs old':9,
'nine-year-old':9,
'Grandchildren ages nine':9,
'boys (nine':9,
'boys(nine':9,
'daughters (nine':9,
'daughters(nine':9,
'girls (nine':9,
'girls(nine':9,
'grandchildren (nine':9,
'grandchildren(nine':9,
'granddaughters (nine':9,
'granddaughters(nine':9,
'grandkids (nine':9,
'grandkids(nine':9,
'grandsons ( nine':9,
'grandsons( nine':9,
'he just turned nine':9,
'he was nine':9,
'is almost nine':9,
'kids ( nine':9,
'kids( nine':9,
'sons ( nine':9,
'sons( nine':9,
'they are nine':9,
'when he turned nine':9,
'when he was nine':9,
'tenth birthday':10,
'10th birthday':10,
'10 y.o':10,
'10 y.o.':10,
'10 y/o':10,
'10 year old':10,
'10 years old':10,
'10 yo':10,
'10 yr ol':10,
'10 yr old':10,
'10 yrs ol':10,
'10 yrs old':10,
'10-year-old':10,
'Grandchildren ages 10':10,
'boys ( 10':10,
'boys( 10':10,
'daughters ( 10':10,
'daughters( 10':10,
'girls ( 10':10,
'girls( 10':10,
'grandchildren ( 10':10,
'grandchildren( 10':10,
'granddaughters ( 10':10,
'granddaughters( 10':10,
'grandkids ( 10':10,
'grandkids( 10':10,
'grandsons ( 10':10,
'grandsons( 10':10,
'he just turned 10':10,
'he was 10':10,
'is almost 10':10,
'kids ( 10':10,
'kids( 10':10,
'sons ( 10':10,
'sons( 10':10,
'they are 10':10,
'when he turned 10':10,
'when he was 10':10,
'ten y/o':10,
'ten year old':10,
'ten years old':10,
'ten yo':10,
'ten yr ol':10,
'ten yr old':10,
'ten yrs ol':10,
'ten yrs old':10,
'ten-year-old':10,
'Grandchildren ages ten':10,
'boys (ten':10,
'boys(ten':10,
'daughters (ten':10,
'daughters(ten':10,
'girls (ten':10,
'girls(ten':10,
'grandchildren (ten':10,
'grandchildren(ten':10,
'granddaughters (ten':10,
'granddaughters(ten':10,
'grandkids (ten':10,
'grandkids(ten':10,
'grandsons ( ten':10,
'grandsons( ten':10,
'he just turned ten':10,
'he was ten':10,
'is almost ten':10,
'kids ( ten':10,
'kids( ten':10,
'sons ( ten':10,
'sons( ten':10,
'they are ten':10,
'when he turned ten':10,
'when he was ten':10,
'eleventh birthday':11,
'11th birthday':11,
'11 y.o':11,
'11 y.o.':11,
'11 y/o':11,
'11 year old':11,
'11 years old':11,
'11 yo':11,
'11 yr ol':11,
'11 yr old':11,
'11 yrs ol':11,
'11 yrs old':11,
'11-year-old':11,
'Grandchildren ages 11':11,
'boys ( 11':11,
'boys( 11':11,
'daughters ( 11':11,
'daughters( 11':11,
'girls ( 11':11,
'girls( 11':11,
'grandchildren ( 11':11,
'grandchildren( 11':11,
'granddaughters ( 11':11,
'granddaughters( 11':11,
'grandkids ( 11':11,
'grandkids( 11':11,
'grandsons ( 11':11,
'grandsons( 11':11,
'he just turned 11':11,
'he was 11':11,
'is almost 11':11,
'kids ( 11':11,
'kids( 11':11,
'sons ( 11':11,
'sons( 11':11,
'they are 11':11,
'when he turned 11':11,
'when he was 11':11,
'eleven y/o':11,
'eleven year old':11,
'eleven years old':11,
'eleven yo':11,
'eleven yr ol':11,
'eleven yr old':11,
'eleven yrs ol':11,
'eleven yrs old':11,
'eleven-year-old':11,
'Grandchildren ages eleven':11,
'boys (eleven':11,
'boys(eleven':11,
'daughters (eleven':11,
'daughters(eleven':11,
'girls (eleven':11,
'girls(eleven':11,
'grandchildren (eleven':11,
'grandchildren(eleven':11,
'granddaughters (eleven':11,
'granddaughters(eleven':11,
'grandkids (eleven':11,
'grandkids(eleven':11,
'grandsons ( eleven':11,
'grandsons( eleven':11,
'he just turned eleven':11,
'he was eleven':11,
'is almost eleven':11,
'kids ( eleven':11,
'kids( eleven':11,
'sons ( eleven':11,
'sons( eleven':11,
'they are eleven':11,
'when he turned eleven':11,
'when he was eleven':11,
'twelfth birthday':12,
'12th birthday':12,
'12 y.o':12,
'12 y.o.':12,
'12 y/o':12,
'12 year old':12,
'12 years old':12,
'12 yo':12,
'12 yr ol':12,
'12 yr old':12,
'12 yrs ol':12,
'12 yrs old':12,
'12-year-old':12,
'Grandchildren ages 12':12,
'boys ( 12':12,
'boys( 12':12,
'daughters ( 12':12,
'daughters( 12':12,
'girls ( 12':12,
'girls( 12':12,
'grandchildren ( 12':12,
'grandchildren( 12':12,
'granddaughters ( 12':12,
'granddaughters( 12':12,
'grandkids ( 12':12,
'grandkids( 12':12,
'grandsons ( 12':12,
'grandsons( 12':12,
'he just turned 12':12,
'he was 12':12,
'is almost 12':12,
'kids ( 12':12,
'kids( 12':12,
'sons ( 12':12,
'sons( 12':12,
'they are 12':12,
'when he turned 12':12,
'when he was 12':12,
'twelve y/o':12,
'twelve year old':12,
'twelve years old':12,
'twelve yo':12,
'twelve yr ol':12,
'twelve yr old':12,
'twelve yrs ol':12,
'twelve yrs old':12,
'twelve-year-old':12,
'Grandchildren ages twelve':12,
'boys (twelve':12,
'boys(twelve':12,
'daughters (twelve':12,
'daughters(twelve':12,
'girls (twelve':12,
'girls(twelve':12,
'grandchildren (twelve':12,
'grandchildren(twelve':12,
'granddaughters (twelve':12,
'granddaughters(twelve':12,
'grandkids (twelve':12,
'grandkids(twelve':12,
'grandsons ( twelve':12,
'grandsons( twelve':12,
'he just turned twelve':12,
'he was twelve':12,
'is almost twelve':12,
'kids ( twelve':12,
'kids( twelve':12,
'sons ( twelve':12,
'sons( twelve':12,
'they are twelve':12,
'when he turned twelve':12,
'when he was twelve':12,
'thirteenth birthday':13,
'13th birthday':13,
'13 y.o':13,
'13 y.o.':13,
'13 y/o':13,
'13 year old':13,
'13 years old':13,
'13 yo':13,
'13 yr ol':13,
'13 yr old':13,
'13 yrs ol':13,
'13 yrs old':13,
'13-year-old':13,
'Grandchildren ages 13':13,
'boys ( 13':13,
'boys( 13':13,
'daughters ( 13':13,
'daughters( 13':13,
'girls ( 13':13,
'girls( 13':13,
'grandchildren ( 13':13,
'grandchildren( 13':13,
'granddaughters ( 13':13,
'granddaughters( 13':13,
'grandkids ( 13':13,
'grandkids( 13':13,
'grandsons ( 13':13,
'grandsons( 13':13,
'he just turned 13':13,
'he was 13':13,
'is almost 13':13,
'kids ( 13':13,
'kids( 13':13,
'sons ( 13':13,
'sons( 13':13,
'they are 13':13,
'when he turned 13':13,
'when he was 13':13,
'thirteen y/o':13,
'thirteen year old':13,
'thirteen years old':13,
'thirteen yo':13,
'thirteen yr ol':13,
'thirteen yr old':13,
'thirteen yrs ol':13,
'thirteen yrs old':13,
'thirteen-year-old':13,
'Grandchildren ages thirteen':13,
'boys (thirteen':13,
'boys(thirteen':13,
'daughters (thirteen':13,
'daughters(thirteen':13,
'girls (thirteen':13,
'girls(thirteen':13,
'grandchildren (thirteen':13,
'grandchildren(thirteen':13,
'granddaughters (thirteen':13,
'granddaughters(thirteen':13,
'grandkids (thirteen':13,
'grandkids(thirteen':13,
'grandsons ( thirteen':13,
'grandsons( thirteen':13,
'he just turned thirteen':13,
'he was thirteen':13,
'is almost thirteen':13,
'kids ( thirteen':13,
'kids( thirteen':13,
'sons ( thirteen':13,
'sons( thirteen':13,
'they are thirteen':13,
'when he turned thirteen':13,
'when he was thirteen':13,
'fourteenth birthday':14,
'14th birthday':14,
'14 y.o':14,
'14 y.o.':14,
'14 y/o':14,
'14 year old':14,
'14 years old':14,
'14 yo':14,
'14 yr ol':14,
'14 yr old':14,
'14 yrs ol':14,
'14 yrs old':14,
'14-year-old':14,
'Grandchildren ages 14':14,
'boys ( 14':14,
'boys( 14':14,
'daughters ( 14':14,
'daughters( 14':14,
'girls ( 14':14,
'girls( 14':14,
'grandchildren ( 14':14,
'grandchildren( 14':14,
'granddaughters ( 14':14,
'granddaughters( 14':14,
'grandkids ( 14':14,
'grandkids( 14':14,
'grandsons ( 14':14,
'grandsons( 14':14,
'he just turned 14':14,
'he was 14':14,
'is almost 14':14,
'kids ( 14':14,
'kids( 14':14,
'sons ( 14':14,
'sons( 14':14,
'they are 14':14,
'when he turned 14':14,
'when he was 14':14,
'fourteen y/o':14,
'fourteen year old':14,
'fourteen years old':14,
'fourteen yo':14,
'fourteen yr ol':14,
'fourteen yr old':14,
'fourteen yrs ol':14,
'fourteen yrs old':14,
'fourteen-year-old':14,
'Grandchildren ages fourteen':14,
'boys (fourteen':14,
'boys(fourteen':14,
'daughters (fourteen':14,
'daughters(fourteen':14,
'girls (fourteen':14,
'girls(fourteen':14,
'grandchildren (fourteen':14,
'grandchildren(fourteen':14,
'granddaughters (fourteen':14,
'granddaughters(fourteen':14,
'grandkids (fourteen':14,
'grandkids(fourteen':14,
'grandsons ( fourteen':14,
'grandsons( fourteen':14,
'he just turned fourteen':14,
'he was fourteen':14,
'is almost fourteen':14,
'kids ( fourteen':14,
'kids( fourteen':14,
'sons ( fourteen':14,
'sons( fourteen':14,
'they are fourteen':14,
'when he turned fourteen':14,
'when he was fourteen':14,
'fifteenth birthday':15,
'15th birthday':15,
'15 y.o':15,
'15 y.o.':15,
'15 y/o':15,
'15 year old':15,
'15 years old':15,
'15 yo':15,
'15 yr ol':15,
'15 yr old':15,
'15 yrs ol':15,
'15 yrs old':15,
'15-year-old':15,
'Grandchildren ages 15':15,
'boys ( 15':15,
'boys( 15':15,
'daughters ( 15':15,
'daughters( 15':15,
'girls ( 15':15,
'girls( 15':15,
'grandchildren ( 15':15,
'grandchildren( 15':15,
'granddaughters ( 15':15,
'granddaughters( 15':15,
'grandkids ( 15':15,
'grandkids( 15':15,
'grandsons ( 15':15,
'grandsons( 15':15,
'he just turned 15':15,
'he was 15':15,
'is almost 15':15,
'kids ( 15':15,
'kids( 15':15,
'sons ( 15':15,
'sons( 15':15,
'they are 15':15,
'when he turned 15':15,
'when he was 15':15,
'fifteen y/o':15,
'fifteen year old':15,
'fifteen years old':15,
'fifteen yo':15,
'fifteen yr ol':15,
'fifteen yr old':15,
'fifteen yrs ol':15,
'fifteen yrs old':15,
'fifteen-year-old':15,
'Grandchildren ages fifteen':15,
'boys (fifteen':15,
'boys(fifteen':15,
'daughters (fifteen':15,
'daughters(fifteen':15,
'girls (fifteen':15,
'girls(fifteen':15,
'grandchildren (fifteen':15,
'grandchildren(fifteen':15,
'granddaughters (fifteen':15,
'granddaughters(fifteen':15,
'grandkids (fifteen':15,
'grandkids(fifteen':15,
'grandsons ( fifteen':15,
'grandsons( fifteen':15,
'he just turned fifteen':15,
'he was fifteen':15,
'is almost fifteen':15,
'kids ( fifteen':15,
'kids( fifteen':15,
'sons ( fifteen':15,
'sons( fifteen':15,
'they are fifteen':15,
'when he turned fifteen':15,
'when he was fifteen':15,
'sixteenth birthday':16,
'16th birthday':16,
'16 y.o':16,
'16 y.o.':16,
'16 y/o':16,
'16 year old':16,
'16 years old':16,
'16 yo':16,
'16 yr ol':16,
'16 yr old':16,
'16 yrs ol':16,
'16 yrs old':16,
'16-year-old':16,
'Grandchildren ages 16':16,
'boys ( 16':16,
'boys( 16':16,
'daughters ( 16':16,
'daughters( 16':16,
'girls ( 16':16,
'girls( 16':16,
'grandchildren ( 16':16,
'grandchildren( 16':16,
'granddaughters ( 16':16,
'granddaughters( 16':16,
'grandkids ( 16':16,
'grandkids( 16':16,
'grandsons ( 16':16,
'grandsons( 16':16,
'he just turned 16':16,
'he was 16':16,
'is almost 16':16,
'kids ( 16':16,
'kids( 16':16,
'sons ( 16':16,
'sons( 16':16,
'they are 16':16,
'when he turned 16':16,
'when he was 16':16,
'sixteen y/o':16,
'sixteen year old':16,
'sixteen years old':16,
'sixteen yo':16,
'sixteen yr ol':16,
'sixteen yr old':16,
'sixteen yrs ol':16,
'sixteen yrs old':16,
'sixteen-year-old':16,
'Grandchildren ages sixteen':16,
'boys (sixteen':16,
'boys(sixteen':16,
'daughters (sixteen':16,
'daughters(sixteen':16,
'girls (sixteen':16,
'girls(sixteen':16,
'grandchildren (sixteen':16,
'grandchildren(sixteen':16,
'granddaughters (sixteen':16,
'granddaughters(sixteen':16,
'grandkids (sixteen':16,
'grandkids(sixteen':16,
'grandsons ( sixteen':16,
'grandsons( sixteen':16,
'he just turned sixteen':16,
'he was sixteen':16,
'is almost sixteen':16,
'kids ( sixteen':16,
'kids( sixteen':16,
'sons ( sixteen':16,
'sons( sixteen':16,
'they are sixteen':16,
'when he turned sixteen':16,
'when he was sixteen':16,
'seventeenth birthday':17,
'17th birthday':17,
'17 y.o':17,
'17 y.o.':17,
'17 y/o':17,
'17 year old':17,
'17 years old':17,
'17 yo':17,
'17 yr ol':17,
'17 yr old':17,
'17 yrs ol':17,
'17 yrs old':17,
'17-year-old':17,
'Grandchildren ages 17':17,
'boys ( 17':17,
'boys( 17':17,
'daughters ( 17':17,
'daughters( 17':17,
'girls ( 17':17,
'girls( 17':17,
'grandchildren ( 17':17,
'grandchildren( 17':17,
'granddaughters ( 17':17,
'granddaughters( 17':17,
'grandkids ( 17':17,
'grandkids( 17':17,
'grandsons ( 17':17,
'grandsons( 17':17,
'he just turned 17':17,
'he was 17':17,
'is almost 17':17,
'kids ( 17':17,
'kids( 17':17,
'sons ( 17':17,
'sons( 17':17,
'they are 17':17,
'when he turned 17':17,
'when he was 17':17,
'seventeen y/o':17,
'seventeen year old':17,
'seventeen years old':17,
'seventeen yo':17,
'seventeen yr ol':17,
'seventeen yr old':17,
'seventeen yrs ol':17,
'seventeen yrs old':17,
'seventeen-year-old':17,
'Grandchildren ages seventeen':17,
'boys (seventeen':17,
'boys(seventeen':17,
'daughters (seventeen':17,
'daughters(seventeen':17,
'girls (seventeen':17,
'girls(seventeen':17,
'grandchildren (seventeen':17,
'grandchildren(seventeen':17,
'granddaughters (seventeen':17,
'granddaughters(seventeen':17,
'grandkids (seventeen':17,
'grandkids(seventeen':17,
'grandsons ( seventeen':17,
'grandsons( seventeen':17,
'he just turned seventeen':17,
'he was seventeen':17,
'is almost seventeen':17,
'kids ( seventeen':17,
'kids( seventeen':17,
'sons ( seventeen':17,
'sons( seventeen':17,
'they are seventeen':17,
'when he turned seventeen':17,
'when he was seventeen':17
}


start_mark = '<div class="reviewText">'
finish_mark = '<div style="padding-top: 10px; clear: both; width: 100%;">'

def grab_ASINs():
	ASIN_list=[]
	with open('../data/ASINListSmallClean.txt','r') as ASINList:
		ASINs_raw = ASINList.readlines()
		ASINs_raw = list(set(ASINs_raw))
		for i in ASINs_raw:
			i = i[:(len(i)-2)]
			ASIN_list.append(i.split(','))

	return ASIN_list


def grab_reviews(my_reviews, start_mark, finish_mark,num_reviews):
	start = 0
	finish = 0
	starts = []
	finishes = []
	point = 0
	text =[]

	while point <num_reviews: #should be number of reviews on page, diff for final page
		start = my_reviews.find(start_mark,start+1)
		finish = my_reviews.find(finish_mark,finish+1)
		starts.append(start+len(start_mark))
		finishes.append(finish)

		point +=1
	for i in range(len(starts)):
		text.append(my_reviews[starts[i]:finishes[i]])
	return text

def parse_reviews(review_text,check_list,ages):
	age = []
	for i in range(len(review_text)):
		for key in check_list:
			if review_text[i].find(key) >=0:
				age.append(int(check_list[key]))
				break

	return age

def sort_ages(ages):
	ages_count=[0]*18
	ages.sort()
	for i in ages:
		ages_count[i]+=1
	return ages_count


def main():
	print_index =0
	#[[name ,ASIN,review_count]]
	ASIN_list= grab_ASINs() 
	with open('../data/name_ASIN_rcount_ages.txt','w') as output:
		for j in ASIN_list:
			ages =[]
			remainder=int(j[2])%10
			if remainder!=0:
				adjusted_review_count = (int(j[2])/ 10)+1
			else:
				adjusted_review_count= int(j[2])/10
			for i in range(adjusted_review_count):
				review_url = first_review_url+j[1]+middle_review_url+str(i+1)+last_review_url
				my_reviews = urllib.urlopen(review_url)
				my_reviews = my_reviews.read()
				if (i+1)>(int(j[2])/10):
					num_reviews=remainder
				else:
					num_reviews=10
				review_text = grab_reviews(my_reviews,start_mark,finish_mark,num_reviews)
				ages = ages+ parse_reviews(review_text,check_list,ages)
			break_down = sort_ages(ages)
			out = str(j[0])+","+str(j[1])+","+str(j[2])+","
			for each in break_down:
				out = out + str(each)+ " "
			out = out + "\n"
			output.write(out)
			print print_index
			print_index +=1
			#print ages

	
	#print float(sum(final_output["B00A8UT562"]))/float(len(final_output["B00A8UT562"]))
	#print float(sum(final_output["B00A8UT55I"]))/float(len(final_output["B00A8UT55I"]))
	#print float(sum(final_output["B00A8UT5TY"]))/float(len(final_output["B00A8UT5TY"]))
	#print float(sum(final_output["B00A8UT558"]))/float(len(final_output["B00A8UT558"]))

main()



