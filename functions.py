from pprint import pprint as pp
def post_list(postIdDict):
    pp(postIdDict)
    postHyperLink = []
    post_group = {}
    for item in sorted(postIdDict, key=lambda x: postIdDict[x][1]['post_group'], reverse=True):
        if postIdDict[item][1]['post_group'] not in post_group:
            post_group[postIdDict[item][1]['post_group']] = True
            postHyperLink.append('## '+postIdDict[item][1]['post_group'])
        postHyperLink.append('* ['+postIdDict[item][1]['post_title']+']'+'('+postIdDict[item][0]+')')
    postHyperLink = '\n'.join(postHyperLink)
    return postHyperLink
