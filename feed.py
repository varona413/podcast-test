import yaml
# Module which implements a simple & efficient API for parsing XML data
import xml.etree.ElementTree as xml_tree

# Open file on read mode (default)
# 'w' = write, 'a' = append, 'b' = binary
with open('feed.yaml', 'r') as file:
    # safe_load() is data-parsing method provided by PyYAML library with enhanced security compared
    # to yaml.load(), as it restricts the type of objects it can construct to Python types
    yaml_data = yaml.safe_load(file)

    # Next, instantiate an XML element tree, a hierarchical representation of an XML doc where its
    # structure is modeled as a tree, and each node corresponds to an XML element
    
    # Add an RSS tag to the extracted RSS element
    rss_element = xml_tree.Element('rss', {'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

# Create sub-element inside rss_element called 'channel'
channel_element = xml_tree.SubElement(rss_element, 'channel')

# Create sub-element inside channel, which parses the data from yaml_data
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'itunes:image').text = yaml_data['image']
xml_tree.SubElement(channel_element, 'language').text = yaml_data['language']

# Create link

# Feed rss_element into output_tree to be processed
output_tree = xml_tree.ElementTree(rss_element)
# Write to new xml file and auto-generate the xml tag
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
