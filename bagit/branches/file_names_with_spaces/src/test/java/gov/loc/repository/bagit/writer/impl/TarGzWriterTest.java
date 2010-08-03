package gov.loc.repository.bagit.writer.impl;

import gov.loc.repository.bagit.utilities.ResourceHelper;
import gov.loc.repository.bagit.writer.Writer;

import java.io.File;

import org.junit.Before;

public class TarGzWriterTest extends AbstractWriterTest {

	File bagFile;
	
	@Before
    @Override
	public void setUp() throws Exception {
		bagFile = new File(ResourceHelper.getFile("bags"), "foo.tar.bz2");
	}

	@Override
	public File getBagFile() {
		return this.bagFile;
	}

	@Override
	public Writer getBagWriter() {
		return new TarGzWriter(bagFactory);
	}

}