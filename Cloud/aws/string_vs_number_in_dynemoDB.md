# String vs Number in dynemodb for floteing value


https://www.reddit.com/r/aws/comments/10jabvb/why_are_people_using_strings_to_represent_numbers/?rdt=63170


DynamoDB supports a number of data types, including strings, numbers, and binary data. By using strings to represent numbers, developers can take advantage of the built-in string sorting and comparison functions in DynamoDB, which can be useful for queries and sorting.

In some cases, the precision of numbers stored in DynamoDB may be limited. By using strings to represent numbers, developers can maintain full precision and avoid losing data due to rounding or truncation errors. Some programming languages, such as JavaScript, do not have a distinct numeric type and instead represent all numbers as double-precision floating-point values. In such cases, using strings to represent numbers in DynamoDB can ensure that the numbers are stored and retrieved with the correct precision. 

DynamoDB does not support number range query, but with string representation of numbers, range queries can be performed by comparing lexicographically. 

It's worth noting that storing numbers as strings can come with some downsides, such as increased storage space and the need to convert the numbers back to their original format when they are used in mathematical operations.


---

https://stackoverflow.com/questions/41968654/amazon-dynamodb-storing-integers-as-numbers-vs-strings

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

From the documentation, if you store a number as 1.999999 you will get it as 1.999999.

Also further documentation:

A Number can have up to 38 digits of precision, and can be positive, negative, or zero.

Positive range: 1E-130 to 9.9999999999999999999999999999999999999E+125 Negative range: -9.9999999999999999999999999999999999999E+125 to -1E-130 DynamoDB uses JSON strings to represent Number data in requests and replies. For more information, see DynamoDB Low-Level API.

If number precision is important, you should pass numbers to DynamoDB using strings that you convert from a number type.

---

For storing price values that require high precision, especially when dealing with floating-point numbers, you have a couple of options in AWS DynamoDB

:Number Type (N): DynamoDB's Number type can store numbers as high precision values. This is generally the recommended approach for storing prices because it allows you to perform numeric operations directly in DynamoDB, such as atomic counters. However, you need to ensure that your application handles the number precision correctly when reading from or writing to the database.


String Type (S): Another approach is to store prices as strings. This method avoids potential issues with floating-point precision and rounding errors. Prices stored as strings will maintain their exact format, but you will need to convert these strings to numbers in your application logic whenever you need to perform calculations.

Best Practice
For most applications dealing with prices, using the Number type is advisable due to its native support for high precision and the ability to perform direct numeric operations. If you choose to use the String type to completely avoid any potential issues with numeric precision, be prepared to handle the conversion and computation in your application logic.

---

For handling price values with a precision of up to 10 decimal places in DynamoDB, you should use the Number type (N). This type is suitable for storing high-precision numeric data, such as financial figures, which require exact decimal representation.When using the Number type in DynamoDB, you can maintain precision in your application by using the decimal.Decimal class in Python. This approach ensures that you avoid the common floating-point precision issues associated with using floating-point numbers directly.Here’s how you can handle such precision in Python when interacting with DynamoDB:

---
size :
Strings are Unicode with UTF-8 binary encoding. The size of a string is (number of UTF-8-encoded bytes of attribute name) + (number of UTF-8-encoded bytes).

Numbers are variable length, with up to 38 significant digits. Leading and trailing zeroes are trimmed. The size of a number is approximately (number of UTF-8-encoded bytes of attribute name) + (1 byte per two significant digits) + (1 byte).


