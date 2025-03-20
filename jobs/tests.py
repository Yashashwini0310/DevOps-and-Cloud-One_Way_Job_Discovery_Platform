import pytest
from jobs.models import Job
from users.models import CustomUser
@pytest.mark.django_db
class TestJobs:
    def setup_method(self):
        """Create a job for testing"""
        # Create a CustomUser first
        self.user = CustomUser.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.job = Job.objects.create(
            title="Software Engineer",
            description="Develop and maintain applications.",
            company="Tech Corp",
            location="Dublin, Ireland",
            salary=60000,
            employer=self.user
        )

    def test_job_creation(self):
        """Test if a job is created successfully"""
        assert self.job.title == "Software Engineer"
        assert self.job.salary == 60000
        assert self.job.company == "Tech Corp"

    def test_job_listing(self, client):
        """Test if jobs are listed correctly"""
        response = client.get("/jobs/")
        assert response.status_code == 200
