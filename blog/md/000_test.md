[toc]

---



# 标题测试

some paragraph

## 标题2

some paragraph

### 标题3

some paragraph

#### 标题4

some paragraph

##### 标题5

some paragraph

###### 标题6

some paragraph



# 引用测试

> A paragraph of text
>
> Another paragraph
>
> - A list
> - with items
> > rua
> > lua


# 加粗与斜体
*This text will be italic*
**This text will be bold**
***This text will be both bold and italic***

# 删除线
这段话~~不应该~~被删掉

# 显示emoji
this is a :smile: smile emoji

# 代码格式

## inline

Here's an idea: why don't we take `SuperiorProject` and turn it into `**Reasonable**Project`.

## blocks
Check out this neat program I wrote:

default:
```
x = 0
x = 2 + 2
what is x
```

python
```python
import numpy as np
np.run()
```

Javascript
```js
var foo = 'bar';
console.log(foo);
```

# 列表
## 无序列表
* rua
* lua
* cua

## 有序列表
1. rua
2. lua
3. cua

---

1. rua
1. rua
1. kua

## checkbox
 - [x] checked list item
 - [ ] unchecked list item

## 列表缩进
1. lua
	* kua
		* bua？
	* rua
1. bua
	1. kua
		1. qua
	2. rua
2. nua
	- [ ] dua
		
		- [ ] eua
		
	- [x] nua
1.  Some code:

    ```js
    var foo = 'bar';
    console.log(foo);
    ```

# 链接
link to <http://www.google.com/>
this is my email <somedude@mail.com>

[Get Showdown!](https://github.com/showdownjs/showdown).

this is a [link to google][1]

[1]: www.google.com


# Images
![Alt text](https://tse3-mm.cn.bing.net/th/id/OIP.z2PaGkEWlzHLdNKXS3BuOAHaEo?w=201&h=125&c=7&o=5&dpr=2&pid=1.7 "title")

## base64 images
![Alt text](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAIAAAA7l
jmRAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAY
SURBVBhXYwCC/2AAZYEoOAMs8Z+BgQEAXdcR7/Q1gssAAAAASUVORK5CYII=)

# 表格
| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| **col 3 is**  | right-aligned | $1600 |
| col 2 is      | *centered*    |   $12 |
| zebra stripes | ~~are neat~~  |    $1 |
|formular|$a=b$|$$c=d$$|
|complex|$\begin{array}{cc|c} a & b & c \\ d & e & f \end{array}$|end|

# html
some markdown **here**

<div>this is *not* **parsed**</div>

However, there are exceptions to this. With `<code>` and `<pre><code>` tags, their contents are always escaped.

some markdown **here** with <code>foo & bar <baz></baz></code>

