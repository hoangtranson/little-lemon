# XML and JSON response types

When it comes to displaying output, an API developer should always allow the client to request the preferred content type, such as JSON or XML. Clients can do this by supplying an additional header called Accept in the request header

## Request headers

Client applications need to send Accept request headers with every HTTP request to receive the output in JSON or XML

JSON

- Accept: application/json

XML

- Accept: application/xml
- Accept: text/xml

## JSON versus XML

JSON or JavaScript Object Notation is a lightweight and dependency-free data format.

XML or Extensible Markup Language is a powerful, tag-based data format. It is similar to HTML. XML data can be fairly complex.

---

The size of JSON data is smaller than XML. So, it takes less bandwidth.

XML data is lengthier than JSON and takes up more bandwidth.

---

JSON data is like keys and values.

```
{
  "author": "Jack London",
  "title": "Seawolf"
}
```

XML is completely tag-based, it does not have key-value pairs like JSON.

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
   <author>Jack London</author>
   <title>Seawolf</title>
</root>
```

---

Representing array elements is simpler in JSON. Here’s an example:

```
{
  "items": [1,2,3,4,5]
}
```

You can still display array elements in XML but it’s very verbose.

```
<?xml version="1.0"
encoding="UTF-8"?>
<root>
   <items>
  	<element>1</element>
  	<element>2</element>
  	<element>3</element>
  	<element>4</element>
    <element>5</element>
   </items>
</root>
```

---

Generating and parsing JSON data is faster than XML and this conversion process requires less memory and computing power.

Generating and parsing XML is a complex process, and it usually takes more processing power and memory than processing JSON.

---

There is no way to include comments in JSON data.

XML data can include comments.
