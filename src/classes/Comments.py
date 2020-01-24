import os

class Comments:

    def __init__(self, comment_url, comment_path, s3BucketName):
        self.comment_url = comment_url
        self.s3BucketName = s3BucketName
        self.comment_path = comment_path

    def downloadAll(self, calendar): 
        for month, year in calendar.dates():
            self.download(month, year)
            self.unzip(date)
            self.toCurrentDirectory(date)
            self.toS3(date)

    def download(self, date):
        os.system( "wget -r --no-parent -A 'RC_%d-%.2d*' %s" \
            %  (year, month, self.comment_url) ) 

    def unzip(self, date):
        os.system('bzip2 -d %s/RC_%d-%.2d.bz2' \
                % (self.comment_path, year, month) )

    def toCurrentDirectory(self, date):
        os.system('mv %s/RC_%d-%.2d .' \
                % (self.comment_path, year, month) )

    def toS3(self, date):
        os.system("aws s3 mv RC_%d-%.2d s3://%s" \
            % (year, month, self.s3BucketName ) )

    def dataFrame(self, context, date):
        return context.read.json("s3a://%s/RC_%d-%.2d" \
                    % (self.s3BucketName, date) )

