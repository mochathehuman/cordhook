def create_embed(
    title=None,
    description=None,
    url=None,
    color=0x5865F2,
    timestamp=None,
    footer_text=None,
    footer_icon_url=None,
    image_url=None,
    thumbnail_url=None,
    author_name=None,
    author_url=None,
    author_icon_url=None,
    fields=None  # list of dicts: [{"name": str, "value": str, "inline": bool}]
):
    embed = {}
    
    if title:
        embed["title"] = title
    if description:
        embed["description"] = description
    if url:
        embed["url"] = url
    if color is not None:
        embed["color"] = color
    if timestamp:
        embed["timestamp"] = timestamp

    if footer_text:
        embed["footer"] = {"text": footer_text}
        if footer_icon_url:
            embed["footer"]["icon_url"] = footer_icon_url

    if image_url:
        embed["image"] = {"url": image_url}
    if thumbnail_url:
        embed["thumbnail"] = {"url": thumbnail_url}

    if author_name:
        embed["author"] = {"name": author_name}
        if author_url:
            embed["author"]["url"] = author_url
        if author_icon_url:
            embed["author"]["icon_url"] = author_icon_url

    if fields:
        embed["fields"] = []
        for f in fields:
            embed["fields"].append({
                "name": f.get("name", "—"),
                "value": f.get("value", "—"),
                "inline": f.get("inline", False)
            })

    return embed
