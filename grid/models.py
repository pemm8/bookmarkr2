# define models for bookmarks & tags
tags = db.Table('tags',
	db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
	db.Column('bookmark_id', db.Integer, db.ForeignKey('bookmark.id'))
)

class Bookmark(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String)
	created_dateb = db.Column(db.DateTime, default=datetime.utcnow)
	image = db.Column(db.String, default='')
	title = db.Column(db.String, default='')
	tags = db.relationship('Tag', secondary=tags, backref=db.backref('bookmarks', lazy='dynamic'))
	public = db.Column(db.Boolean, default=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	class Meta:
		ordering = (('created_date', 'desc'),)

	# def fetch_image(self):
	# 	url_hash = hashlib.md5(self.url).hexdigest()
	# 	filename = 'bookmark-%s.png' % url_hash

	# 	outfile = os.path.join(MEDIA_ROOT, filename)
	# 	params = [PHANTOM, SCRIPT, self.url, outfile]

	# 	exitcode = subprocess.call(params)
	# 	if exitcode == 0:
	# 		self.image = os.path.join(MEDIA_URL, filename)

	def fetch_image(self):
		url_hash = hashlib.md5(self.url).hexdigest()
		filename = 'bookmark-%s.png' % url_hash
		outfile = os.path.join(MEDIA_ROOT, filename)

		fetchimage_async.delay(self.url, outfile)

		self.image = os.path.join(MEDIA_URL, filename)

class Tag(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __str__(self):
		return self.name